/*
* Copyright (c) 2006-2009 Erin Catto http://www.box2d.org
*
* This software is provided 'as-is', without any express or implied
* warranty.  In no event will the authors be held liable for any damages
* arising from the use of this software.
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
* 1. The origin of this software must not be misrepresented; you must not
* claim that you wrote the original software. If you use this software
* in a product, an acknowledgment in the product documentation would be
* appreciated but is not required.
* 2. Altered source versions must be plainly marked as such, and must not be
* misrepresented as being the original software.
* 3. This notice may not be removed or altered from any source distribution.
*/

/* 
 * Base code for CS 296 Software Systems Lab 
 * Department of Computer Science and Engineering, IIT Bombay
 * Instructor: Parag Chaudhuri
 */


#include "cs296_base.hpp"
#include "render.hpp"

#ifdef __APPLE__
	#include <GLUT/glut.h>
#else
	#include "GL/freeglut.h"
#endif

#include <cstring>
using namespace std;

#include "dominos.hpp"

namespace cs296
{
  /**  
   * The is the constructor 
   * This is the documentation block for the constructor.
   */ 
  
  dominos_t::dominos_t()
  {
    //Ground
    /*!  
     * \section sec Blocks of objects
     * \subsection a17 common datatypes
     * There are some common data types used repeatedly.
     * There are data types used in defining the shape of object more precisely entity such as
     * \li \b "b2EdgeShape" for shapes resembling edges or line segments.This class has Set(float,float) 
     * as a member function,it takes the starting and the ending positions as inputs giving the line joining them as output.
     * \li \b "b2PolygonShape" for defining Polygons.This class contains SetasBox(float,float) as a member function to set the width 
     * and height of the box if the shape is a rectangle.
     * \li \b "b2CircleShape" for defining Circles,so it obviously will have radius(float),center(vec2(float,float)) variables in it.
     * 
     * \b "b2RevoluteJointDef" is datatype for defining revolute joints. It is created using
     * a member function Initialise(bodyA, bodyB, anchor).
     * 
     * \b m_world defines the world in which the objects interact.It basically is the universe in which the entities are present.
     * There can be multiple worlds.
     * 
     * \b "b2BodyDef" is the data type used to define the body.
     * 
     * \b "b2FixtureDef" defines the fixture of the body.Fixture is defined for a particular Body.It contains the properties of the 
     * body such as mass,restitution,state etc,mostly everything except the dimensions of the body(that is shape).
     * 
     * \b "CreateFixture" helps Create a fixture which is defined with some particular propreties.
     * 
     */ 
    b2Body* b1;  
    {
      /*!
       * \subsection a16 Ground
       * \li \b "b1" is the pointer to the class which contains the properties of Ground like its fixture,shape and state.
       * \li \b "shape" defines its shape,here it is a line segment so b2EdgeShape is used.
       * \li \b "bd" variable sets the body of Ground. 
       */
      b2EdgeShape shape; 
      shape.Set(b2Vec2(-90.0f, 0.0f), b2Vec2(90.0f, 0.0f));
      b2BodyDef bd; 
      b1 = m_world->CreateBody(&bd); 
      b1->CreateFixture(&shape, 0.0f);
    }
          
    //Top horizontal shelf
    {
	  /*!
	   * \subsection a15 Top horizontal shelf
	   *  This is the horizontal shelf which supports the dominoes.
	   * \li variable \b "shape" as usual is the shape of the body.
	   * \li variable \b "bd" defines the Body of the shelf.
	   */
      b2PolygonShape shape;
      shape.SetAsBox(6.0f, 0.25f);
	
      b2BodyDef bd;
      bd.position.Set(-31.0f, 30.0f);
      b2Body* ground = m_world->CreateBody(&bd);
      ground->CreateFixture(&shape, 0.0f);
    }

    //Dominos
    {
	  /*!
	   * \subsection a14 Dominoes
	   *  Here the ten dominoes which are placed side by side are created.
	   * \li varible \b "fd" is the fixture of a particular domino(all dominoes has same fixture).
	   * \li varible \b "bd" is the body of a domino.
	   * \li variable \b "shape" defines the shape of the domino which is a rectangle or box.
	  */
      b2PolygonShape shape;
      shape.SetAsBox(0.1f, 1.0f);
	
      b2FixtureDef fd;
      fd.shape = &shape;
      fd.density = 20.0f;
      fd.friction = 0.1f;
		
      for (int i = 0; i < 10; ++i)
	{
	  b2BodyDef bd;
	  bd.type = b2_dynamicBody;
	  bd.position.Set(-35.5f + 1.0f * i, 31.25f);
	  b2Body* body = m_world->CreateBody(&bd);
	  body->CreateFixture(&fd);
	}
    }
      
    //Another horizontal shelf
    {
	  /*!
	   * \subsection a13 Another horizontal shelf
	   *  Here the shelf which supports the spheres is created.
	   * \li variable \b "shape" defines the shape of the shelf that is a box.
	   * \li varible \b "bd" is the body of the shelf.
	   */
      b2PolygonShape shape;
      shape.SetAsBox(7.0f, 0.25f);
	//b2Vec2(-20.f,20.f),  0.0f
      b2BodyDef bd;
      bd.position.Set(-19.f,26.f); //initial 1.0f, 6.0f
      b2Body* ground = m_world->CreateBody(&bd);
      ground->CreateFixture(&shape, 0.0f);
    }


    //The pendulum that knocks the dominos off
    {
		/*!
		 * \subsection a12 Pendulum
		 *  Here the pendulum is created
		 * \li bodies \b "b2" \b "b4" helps to create the hinge or anchor.
		 * \li variable \b "jd" defines the joint.
		 * \li varable \b "shape" defines the shape of objects,boxes. 
		 */
      b2Body* b2;
      {
	b2PolygonShape shape;
	shape.SetAsBox(0.25f, 1.5f);
	  
	b2BodyDef bd;
	bd.position.Set(-37.0f, 40.0f);
	b2 = m_world->CreateBody(&bd);
	//b2->CreateFixture(&shape, 10.0f);
      }
	
      b2Body* b4;
      {
	b2PolygonShape shape;
	shape.SetAsBox(0.25f, 0.25f);
	  
	b2BodyDef bd;
	bd.type = b2_dynamicBody;
	bd.position.Set(-40.0f, 33.0f);
	b4 = m_world->CreateBody(&bd);
	b4->CreateFixture(&shape, 2.0f);
      }
	
      b2RevoluteJointDef jd;
      b2Vec2 anchor;
      anchor.Set(-37.0f, 40.0f);
      jd.Initialize(b2, b4, anchor);
      m_world->CreateJoint(&jd);
    }
      
    //The train of small spheres
    {
		/*!
		 * \subsection a11 Train of spheres
		 *  Here the train of small spheres is created.
		 * \li variable \b "circle" defines the shape of the sphere,every sphere has the same shape.
		 * \li varible \b "ballfd" defines the fixture of the sphere.
		 * \li varible \b "ballbd" defines the body of a particular sphere.
		 */
      b2Body* spherebody;
	
      b2CircleShape circle;
      circle.m_radius = 0.5;
	
      b2FixtureDef ballfd;
      ballfd.shape = &circle;
      ballfd.density = 3.0f;
      ballfd.friction = 0.0f;
      ballfd.restitution = 0.0f;
	
      for (int i = 0; i < 10; ++i)
	{
	  b2BodyDef ballbd;
	  ballbd.type = b2_dynamicBody;
	  ballbd.position.Set(-22.2f + i*1.0, 26.6f);
	  spherebody = m_world->CreateBody(&ballbd);
	  spherebody->CreateFixture(&ballfd);
	}
    }
    
    //New ball on the top
    {
	  /*!
	   * \subsection  10 Additional ball
	   *  Here the ball which rolls on the arc is created.
	   * \li variable \b "circle" defines the shape of the sphere,every sphere has the same shape.
	   * \li varible \b "ballfd" defines the fixture of the sphere.
	   * \li varible \b "ballbd" defines the body of a particular sphere.
	   */
	  b2Body* sphere;
	  b2CircleShape circle;
	  circle.m_radius=1.0;
	  b2FixtureDef ballfd;
	  ballfd.shape=&circle;
	  ballfd.density = 5.0f;
      ballfd.friction = 1.0f;
      ballfd.restitution = 0.5f;
      b2BodyDef ballbd;
      ballbd.type=b2_dynamicBody;
      ballbd.position.Set(-25.f,27.f);
      sphere=m_world->CreateBody(&ballbd);
      sphere->CreateFixture(&ballfd);
    }
   
    //Semicircular platform  
    {   
		/*!
		 * \subsection a9 Arc
		 *  Here the quarter-circular platform is creted.
		 * \li varibles \b "x",\b "y" which are of data types float are the cordinated of the centre of cicle and varible \b "r"(float) is radius of the cicle.
		 * \li This arc is created using many small line segments.These line segments are connected in a particular fashion to get this arc.
		 * \li varible \b "semc" defines the shape of a particular line segment.
		 * \li variable \b "bd" refers to the body of line segment.
		 */
		b2Body* b2;
		float x = -36.3f;
		float y = 24.0f;
		float r = 10.0f;
		for(float i=0; i<100; i++)
		{	
			b2EdgeShape semc;
			semc.Set(b2Vec2((x+(r * (cos (3.1415926*i/200.0)))),(y - (r *(sin (3.1415926*i/200.0))))),
					 b2Vec2((x+(r * (cos (3.1415926*(i+1)/200.0)))),(y - (r *(sin (3.1415926*(i+1)/200.0))))));
			b2BodyDef bd;
			b2 = m_world->CreateBody(&bd);
			b2->CreateFixture(&semc, 0.0f);
		}
	}
	
   
       //The pulley system
    {
	  /*!
	   * \subsection a8 Pulley system
	   * Here the pulley system including the open box on the left and horizontal plank on the right are created.
	   */
      b2BodyDef *bd = new b2BodyDef;
      bd->type = b2_dynamicBody;
      bd->position.Set(-10,15);
      bd->fixedRotation = true;
      
      //The open box
      /*!This is the open box.
       * \li varibles \b "fd1" \b "fd2" and \b "fd3" are fixtures of the three sides of the box.
       * \li similarly \b "bs1" \b "bs2" and \b "bs3" are their respective shapes,they are rectangles(boxes).
       */
      b2FixtureDef *fd1 = new b2FixtureDef;
      fd1->density = 10.0;
      fd1->friction = 0.5;
      fd1->restitution = 0.f;
      fd1->shape = new b2PolygonShape;
      b2PolygonShape bs1;
      bs1.SetAsBox(2,0.2, b2Vec2(0.f,-1.9f), 0);
      fd1->shape = &bs1;
      b2FixtureDef *fd2 = new b2FixtureDef;
      fd2->density = 10.0;
      fd2->friction = 0.5;
      fd2->restitution = 0.f;
      fd2->shape = new b2PolygonShape;
      b2PolygonShape bs2;
      bs2.SetAsBox(0.2,2, b2Vec2(2.0f,0.f), 0);
      fd2->shape = &bs2;
      b2FixtureDef *fd3 = new b2FixtureDef;
      fd3->density = 10.0;
      fd3->friction = 0.5;
      fd3->restitution = 0.f;
      fd3->shape = new b2PolygonShape;
      b2PolygonShape bs3;
      bs3.SetAsBox(0.2,2, b2Vec2(-2.0f,0.f), 0);
      fd3->shape = &bs3;
       
      b2Body* box1 = m_world->CreateBody(bd);
      box1->CreateFixture(fd1);
      box1->CreateFixture(fd2);
      box1->CreateFixture(fd3);

      //The bar
      /*!This is the horizontal bar.
       * \li varible \b "bd" is the body of the bar.
       * \li as this bar is similar to the base of the open box in shape so its fixture can be used that is \b fd1.
       */
      bd->position.Set(10,15);	
      fd1->density = 34.0;	  
      b2Body* box2 = m_world->CreateBody(bd);
      box2->CreateFixture(fd1);

      // The pulley joint
      /*!This is the pulley joint.
       * \li variable \b "myjoint" defines the joint .
       * \li \b worldAnchorsGround gives the anchor points w.r.t ground.These are static points and gives the joints of the pulley.
       * \li \b ratio is the pulley ratio, used to simulate a block-and-tackle. 
       */
      b2PulleyJointDef* myjoint = new b2PulleyJointDef();
      //b2Vec2 worldAnchorOnBody1(-10, 15); // Anchor point on body 1 in world axis
      //b2Vec2 worldAnchorOnBody2(10, 15); // Anchor point on body 2 in world axis
      b2Vec2 worldAnchorGround1(-10, 20); // Anchor point for ground 1 in world axis
      b2Vec2 worldAnchorGround2(10, 20); // Anchor point for ground 2 in world axis
      float32 ratio = 1.0f; // Define ratio
      myjoint->Initialize(box1, box2, worldAnchorGround1, worldAnchorGround2, box1->GetWorldCenter(), box2->GetWorldCenter(), ratio);
      m_world->CreateJoint(myjoint);
    }

    //The revolving horizontal platform
    {
	  /*!
	   * \subsection a7 The revolving horizontal platform
	   * Here the revolving platform is created
	   * \li varibles \b "shape" and \b "shape2" defines the shape of the two platforms,a rectangle.One of the platform doesn't have a fixture so it is not visible.
	   * \li variables \b "bd" and \b "bd2" defines the body of these platforms.
	   * \li varible \b "fd" is a pointer to the fixture of the visible body.
	   * \li variable \b "jointDef" defines the joint or point about which the body rotates. 
	   */
      b2PolygonShape shape;
      shape.SetAsBox(2.2f, 0.2f);
	
      b2BodyDef bd;
      bd.position.Set(14.0f, 14.0f);
      bd.type = b2_dynamicBody;
      b2Body* body = m_world->CreateBody(&bd);
      b2FixtureDef *fd = new b2FixtureDef;
      fd->density = 1.f;
      fd->shape = new b2PolygonShape;
      fd->shape = &shape;
      body->CreateFixture(fd);

      b2PolygonShape shape2;
      shape2.SetAsBox(0.2f, 2.0f);
      b2BodyDef bd2;
      bd2.position.Set(14.0f, 16.0f);
      b2Body* body2 = m_world->CreateBody(&bd2); 
   /*   b2FixtureDef *fd2 = new b2FixtureDef;
      fd2->density = 1.f;
      fd2->shape = new b2PolygonShape;
      fd2->shape = &shape2;
      body->CreateFixture(fd2);
  */
      b2RevoluteJointDef jointDef;
      jointDef.bodyA = body;
      jointDef.bodyB = body2;
      jointDef.localAnchorA.Set(0,0);
	  jointDef.localAnchorB.Set(0,0);
      jointDef.collideConnected = false;
      m_world->CreateJoint(&jointDef);
    }
    //The heavy sphere on the platform
    {
	  /*!
	   * \subsection a6 heavy sphere on the platform
	   * Here the sphere on the rotating platform is created.
	   * \li varible \b "Circle" defines the shape of the shere,a circle.
	   * \li varible \b "ballfd" defines the fixture of the sphere.
	   * \li variable \b "ballbd" defines the body of the sphere. 
	   */
      b2Body* sbody;
      b2CircleShape circle;
      circle.m_radius = 1.0;
	
      b2FixtureDef ballfd;
      ballfd.shape = &circle;
      ballfd.density = 150.0f;
      ballfd.friction = 0.0f;
      ballfd.restitution = 0.0f;
      b2BodyDef ballbd;
      ballbd.type = b2_dynamicBody;
      ballbd.position.Set(14.0f, 18.0f);
      sbody = m_world->CreateBody(&ballbd);
      sbody->CreateFixture(&ballfd);
    }
    
    //New sphere at the end
    {
	  /*!
	   * \subsection a5 New sphere at the end
	   *  Here the ball which climbs the plank is created.
	   * \li varible \b "circle" difines the shape of the ball,a circle.
	   * \li variable \b "ballfd" defines the fixture of the ball
	   * \li varible \b "ballbd" defines the body of the ball
	   */
	  b2Body* sphere;
	  b2CircleShape circle;
	  circle.m_radius=1.0;
	  
	  b2FixtureDef ballfd;
	  ballfd.shape=&circle;
	  ballfd.density=0.0000001f;
	  ballfd.friction=0.0f;
	  ballfd.restitution=1.0f;
	  b2BodyDef ballbd;
	  ballbd.type=b2_dynamicBody;
	  ballbd.position.Set(10.0f,1.0f);
	  sphere = m_world->CreateBody(&ballbd);
	  sphere->CreateFixture(&ballfd);
    }


    //The see-saw system at the bottom
    {
      //The triangle wedge
      /*!
       * \subsection a4 The triangular wedge
       * Here the triangular wedge on which the plank is present is created.
       * \li varible \b "poly" defines the body of the wedge,the shape here is a polygon(triangle).
       * \li varible "vertices" is if type \b "b2vec2" that is it is a vector of two dimensions.
       * \li variable \b "wedgefd" defines the fixturer of this wedge.like its density etc.
       */
      b2Body* sbody;
      b2PolygonShape poly;
      b2Vec2 vertices[3];
      vertices[0].Set(-1,0);
      vertices[1].Set(1,0);
      vertices[2].Set(0,1.5);
      poly.Set(vertices, 3);
      b2FixtureDef wedgefd;
      wedgefd.shape = &poly;
      wedgefd.density = 10.0f;
      wedgefd.friction = 0.0f;
      wedgefd.restitution = 0.0f;
      b2BodyDef wedgebd;
      wedgebd.position.Set(30.0f, 0.0f);
      sbody = m_world->CreateBody(&wedgebd);
      sbody->CreateFixture(&wedgefd);

      //The plank on top of the wedge
      /*!
       * \subsection  a3 Plank on top of the wedge.
       * Here the see-saw plank is created.
       * \li varible \b "shape" defines the shape of this plank.Shape of plank is a box.
       * \li varible \b "bd2" defines the body of this plank.
       * 
       */
      b2PolygonShape shape;
      shape.SetAsBox(15.0f, 0.2f);
      b2BodyDef bd2;
      bd2.position.Set(30.0f, 1.5f);
      bd2.type = b2_dynamicBody;
      b2Body* body = m_world->CreateBody(&bd2);
      b2FixtureDef *fd2 = new b2FixtureDef;
      fd2->density = 1.f;
      fd2->shape = new b2PolygonShape;
      fd2->shape = &shape;
      body->CreateFixture(fd2);

      b2RevoluteJointDef jd;
      b2Vec2 anchor;
      anchor.Set(30.0f, 1.5f);
      jd.Initialize(sbody, body, anchor);
      m_world->CreateJoint(&jd);

      //The light box on the right side of the see-saw
      /*!
       * \subsection  a2 light box
       * Here the box on the right side of see-saw is created.
       * \li varible \b "shape2" defines the shape of the box,rectangle.
       * \li varible \b "bd3" is the body of the box.
       * \li varible \b "fd3" defines the fixture of the box.
       */
      b2PolygonShape shape2;
      shape2.SetAsBox(2.0f, 2.0f);
      b2BodyDef bd3;
      bd3.position.Set(40.0f, 2.0f);
      bd3.type = b2_dynamicBody;
      b2Body* body3 = m_world->CreateBody(&bd3);
      b2FixtureDef *fd3 = new b2FixtureDef;
      fd3->density = 0.01f;
      fd3->shape = new b2PolygonShape;
      fd3->shape = &shape2;
      body3->CreateFixture(fd3);
    }
    
    //Wedge at the end
    {
	  /*!
	   * \subsection  a1 Wedge at the end
	   * Here the wedge present on the ground is created.
	   * \li varible \b "poly" defines the shape of the wedge which is a triangle a subset of the class polygon.
	   * \li varible \b "vertices" is of data type \b "b2Vec2" which represents a vector of two dimensions. 
	   * \li \b Set is a member function used to set the values of b2Vec2 and polygon.
	   * \li varible \b "wedgefd" defines the fixture of wedge.
	   * \li varible \b "wedgebd" defines the body of wedge.
	   */
	  b2Body *wedge;
	  b2PolygonShape poly;
	  b2Vec2 vertices[3];
	  vertices[0].Set(0,0);
	  vertices[1].Set(0,2);
	  vertices[2].Set(8,0);
	  poly.Set(vertices,3);
	  b2FixtureDef wedgefd;
	  wedgefd.shape=&poly;
	  wedgefd.density = 10.0f;
      wedgefd.friction = 0.0f;
      wedgefd.restitution = 0.0f;
      b2BodyDef wedgebd;
      wedgebd.position.Set(-20.0f,0.f);
      wedge=m_world->CreateBody(&wedgebd);
      wedge->CreateFixture(&wedgefd);
  }
      
	   
  }

  sim_t *sim = new sim_t("Dominos", dominos_t::create);
}
